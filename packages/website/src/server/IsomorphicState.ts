import { WebpackServerState } from 'express-isomorphic-extension/webpack';

export default class IsomorphicState implements WebpackServerState {
  assets: string[];
  builtAt: number;
  publicPath: string;
}
